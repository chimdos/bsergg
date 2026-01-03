<?php

namespace App\Filament\Resources\Performances\Schemas;

use Filament\Forms\Components\TextInput;
use Filament\Forms\Components\Toggle;
use Filament\Schemas\Schema;

class PerformanceForm
{
    public static function configure(Schema $schema): Schema
    {
        return $schema
            ->components([
                TextInput::make('game_id')
                    ->required()
                    ->numeric(),
                TextInput::make('player_id')
                    ->required()
                    ->numeric(),
                TextInput::make('brawler_name')
                    ->required(),
                TextInput::make('kills')
                    ->required()
                    ->numeric()
                    ->default(0),
                TextInput::make('deaths')
                    ->required()
                    ->numeric()
                    ->default(0),
                TextInput::make('damage_dealt')
                    ->required()
                    ->numeric()
                    ->default(0),
                TextInput::make('damage_received')
                    ->required()
                    ->numeric()
                    ->default(0),
                TextInput::make('damage_to_safe')
                    ->required()
                    ->numeric()
                    ->default(0),
                TextInput::make('rating_bser')
                    ->required()
                    ->numeric()
                    ->default(0),
                Toggle::make('is_win')
                    ->required(),
            ]);
    }
}
