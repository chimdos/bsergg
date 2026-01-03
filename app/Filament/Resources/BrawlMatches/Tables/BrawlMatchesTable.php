<?php

namespace App\Filament\Resources\BrawlMatches\Tables;

use Filament\Actions\BulkActionGroup;
use Filament\Actions\DeleteBulkAction;
use Filament\Actions\EditAction;
use Filament\Tables\Columns\TextColumn;
use Filament\Tables\Table;

class BrawlMatchesTable
{
    public static function configure(Table $table): Table
    {
        return $table
            ->columns([
                TextColumn::make('tournament_name')
                    ->searchable(),
                TextColumn::make('team_a_id')
                    ->numeric()
                    ->sortable(),
                TextColumn::make('team_b_id')
                    ->numeric()
                    ->sortable(),
                TextColumn::make('score_a')
                    ->numeric()
                    ->sortable(),
                TextColumn::make('score_b')
                    ->numeric()
                    ->sortable(),
                TextColumn::make('played_at')
                    ->dateTime()
                    ->sortable(),
                TextColumn::make('created_at')
                    ->dateTime()
                    ->sortable()
                    ->toggleable(isToggledHiddenByDefault: true),
                TextColumn::make('updated_at')
                    ->dateTime()
                    ->sortable()
                    ->toggleable(isToggledHiddenByDefault: true),
            ])
            ->filters([
                //
            ])
            ->recordActions([
                EditAction::make(),
            ])
            ->toolbarActions([
                BulkActionGroup::make([
                    DeleteBulkAction::make(),
                ]),
            ]);
    }
}
