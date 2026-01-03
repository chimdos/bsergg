<?php

namespace App\Filament\Resources\Performances;

use App\Filament\Resources\Performances\Pages\CreatePerformance;
use App\Filament\Resources\Performances\Pages\EditPerformance;
use App\Filament\Resources\Performances\Pages\ListPerformances;
use App\Models\Performance;
use Filament\Resources\Resource;
use Filament\Schemas\Schema;
use Filament\Tables;
use Filament\Tables\Table;
// Namespaces corretos para o Filament v4:
use Filament\Schemas\Components\Grid;
use Filament\Schemas\Components\Section;
use Filament\Forms\Components\Select;
use Filament\Forms\Components\TextInput;
use Filament\Forms\Components\Toggle;
use Filament\Tables\Columns\TextColumn;
use Filament\Tables\Columns\IconColumn;

class PerformanceResource extends Resource
{
    protected static ?string $model = Performance::class;

    protected static string | \BackedEnum | null $navigationIcon = 'heroicon-o-chart-bar';

    public static function form(Schema $schema): Schema
    {
        return $schema
            ->components([
                Grid::make(3)
                    ->schema([
                        Section::make('Contexto do Jogo')
                            ->columnSpan(1)
                            ->schema([
                                Select::make('game_id')
                                    ->relationship('game', 'map_name')
                                    ->label('Mapa/Set')
                                    ->required()
                                    ->searchable()
                                    ->preload(),
                                Select::make('player_id')
                                    ->relationship('player', 'name')
                                    ->label('Jogador')
                                    ->required()
                                    ->searchable()
                                    ->preload(),
                                TextInput::make('brawler_name')
                                    ->label('Brawler')
                                    ->required(),
                                Toggle::make('is_win')
                                    ->label('Vitória?')
                                    ->onColor('success'),
                            ]),

                        Section::make('Estatísticas de Combate')
                            ->columnSpan(2)
                            ->schema([
                                Grid::make(2)->schema([
                                    TextInput::make('kills')
                                        ->numeric()
                                        ->default(0)
                                        ->required(),
                                    TextInput::make('deaths')
                                        ->numeric()
                                        ->default(0)
                                        ->required(),
                                    TextInput::make('damage_dealt')
                                        ->numeric()
                                        ->label('DPS')
                                        ->default(0),
                                    TextInput::make('damage_received')
                                        ->numeric()
                                        ->label('Damage Received')
                                        ->default(0),
                                    TextInput::make('healing')
                                        ->numeric()
                                        ->label('Healing')
                                        ->default(0),
                                    TextInput::make('damage_to_safe')
                                        ->numeric()
                                        ->label('Damage to Safe')
                                        ->default(0),
                                ]),
                                
                                TextInput::make('rating_bser')
                                    ->numeric()
                                    ->label('Rating 1.0')
                                    ->helperText('Insira o valor do rating')
                                    ->required()
                                    ->extraInputAttributes(['style' => 'font-size: 1.5rem; font-weight: bold; color: #fbbf24;']),
                            ]),
                    ])
            ]);
    }

    public static function table(Table $table): Table
    {
        return $table
            ->columns([
                TextColumn::make('player.name')
                    ->label('Player')
                    ->sortable()
                    ->searchable(),
                TextColumn::make('brawler_name')
                    ->label('Brawler'),
                TextColumn::make('game.map_name')
                    ->label('Map'),
                TextColumn::make('rating_bser')
                    ->label('Rating 1.0')
                    ->badge()
                    ->color(fn (string $state): string => match (true) {
                        (float)$state >= 1.20 => 'success',
                        (float)$state < 0.85 => 'danger',
                        default => 'warning',
                    })
                    ->sortable(),
                IconColumn::make('is_win')
                    ->boolean()
                    ->label('W'),
            ])
            ->defaultSort('created_at', 'desc');
    }

    public static function getPages(): array
    {
        return [
            'index' => ListPerformances::route('/'),
            'create' => CreatePerformance::route('/create'),
            'edit' => EditPerformance::route('/{record}/edit'),
        ];
    }
}